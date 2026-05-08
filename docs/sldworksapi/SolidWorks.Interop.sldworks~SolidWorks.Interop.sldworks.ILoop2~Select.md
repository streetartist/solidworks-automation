# Select Method (ILoop2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2~Select`

Selects a loop in the graphics area.
Selects a loop in the graphics area.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Select( _
   ByVal Edge As System.Object, _
   ByVal Append As System.Boolean, _
   ByVal SelectionData As System.Object _
) As System.Boolean
```

```

Dim instance As ILoop2
Dim Edge As System.Object
Dim Append As System.Boolean
Dim SelectionData As System.Object
Dim value As System.Boolean
 
value = instance.Select(Edge, Append, SelectionData)
```

```

System.bool Select( 
   System.object Edge,
   System.bool Append,
   System.object SelectionData
)
```

```

System.bool Select( 
   System.Object^ Edge,
   System.bool Append,
   System.Object^ SelectionData
) 
```

#### Parameters

*Edge*
:   [Edge](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IEdge.md) of the loop (see **Remarks**)

*Append*
:   True to append this selection to the selection list, false to replace the selection list with this selection

*SelectionData*
:   [ISelectData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectData.md) object

#### Return Value

True if the loop is selected, false if not

Remarks

This loop can share Edge with an adjacent loop, if it exists.

If Edge is:

- a valid edge on this loop, this method selects the adjacent loop.
- Nothing or null, this method selects this loop.

Example

'VBA

'============================================

' Preconditions:

' 1. Open a model with a triangular face.

' 2. Multi-select the triangular face and one of its edges.

' 3. Comment out one of the highlighted lines with **swLoop.Select**.

' 4. Run the macro.

' 5. Comment out the other highlighted line.

' 6. Run the macro again.

' Postconditions:

' 1. Inspect the Immediate window after each run.

' 2. Notice that a different loop is selected each time.

'============================================

Option Explicit

Sub main()  
    Dim swApp As SldWorks.SldWorks  
    Set swApp = Application.SldWorks  
     
    Dim swModel As ModelDoc2  
    Set swModel = swApp.ActiveDoc  
    If swModel Is Nothing Then Exit Sub  
     
    Dim swSelMgr As SelectionMgr  
    Set swSelMgr = swModel.SelectionManager  
     
    Dim swFace As Face2  
    Dim swEdge As Edge  
     
    Dim iSel As Long  
    For iSel = 1 To 2  
        Select Case swSelMgr.GetSelectedObjectType3(iSel, -1)  
        Case swSelFACES  
            Set swFace = swSelMgr.GetSelectedObject6(iSel, -1)  
        Case swSelEDGES  
            Set swEdge = swSelMgr.GetSelectedObject6(iSel, -1)  
        End Select  
    Next  
     
    If swFace Is Nothing Or swEdge Is Nothing Then Exit Sub  
     
    Dim vLoops As Variant  
    vLoops = swFace.**GetLoops**()  
     
    Dim vLoop As Variant  
    Dim swLoop As Loop2  
    For Each vLoop In vLoops  
        Set swLoop = vLoop  
        Dim vEdges As Variant  
        vEdges = swLoop.**GetEdges**()  
         
        Dim loopUsesEdges As Boolean  
        loopUsesEdges = False  
        Dim vEdge As Variant  
        For Each vEdge In vEdges  
            If vEdge Is swEdge Then  
                loopUsesEdges = True  
                Exit For  
            End If  
        Next  
        If loopUsesEdges Then  
            ' Demonstrate that we have the right loop..  
            Debug.Assert swLoop.**GetFace** Is swFace  
            swModel.ClearSelection2 True  
            For Each vEdge In vEdges  
                Dim swLoopEdge As Entity  
                Set swLoopEdge = vEdge  
                swLoopEdge.Select4 True, Nothing  
            Next  
            Exit For  
        Else  
            Set swLoop = Nothing  
        End If  
    Next  
     
    Stop ' Examine highlighted edges of this loop  
     
    If Not swLoop Is Nothing Then  
        Debug.Print "Loop has " & swLoop.**GetEdgeCount**() & " edges."  
     
        Dim bResult As Boolean

**' Comment and uncomment out different lines after each run:** **bResult = swLoop.Select(swEdge, False, Nothing) 'Selects the adjacent loop  
        'bResult = swLoop.Select(Nothing, False, Nothing) 'Selects this loop**         
        Stop ' Examine highlighted edges of selected loop. This loop or its adjacent loop?  
         
        Dim swSelLoop As Loop2  
        Set swSelLoop = swSelMgr.**GetSelectedObjectLoop2**(1, -1)  
         
        Debug.Print "Selected loop has " & swSelLoop.**GetEdgeCount**() & " edges."  
                 
        swModel.ClearSelection2 True  
        vEdge = vbEmpty  
        vEdge = swSelLoop.**GetEdges**()  
         
        For Each vEdge In vEdges  
             
            Set swLoopEdge = vEdge  
            swLoopEdge.Select4 True, Nothing  
        Next  
        Debug.Print "Selected " & swSelMgr.GetSelectedObjectCount2(-1) & " edges in loop."  
    End If  
     
End Sub

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILoop2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2.md)  
[ILoop2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILoop2_members.md)  
[DPartDocEvents\_FlipLoopNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DPartDocEvents_FlipLoopNotifyEventHandler.md)  
[DAssemblyDocEvents\_FileDropNotifyEventHandler Delegate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.DAssemblyDocEvents_FileDropNotifyEventHandler.md)
