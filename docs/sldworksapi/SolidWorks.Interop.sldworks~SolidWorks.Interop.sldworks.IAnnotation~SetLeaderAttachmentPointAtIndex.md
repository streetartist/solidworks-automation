# SetLeaderAttachmentPointAtIndex Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeaderAttachmentPointAtIndex`

Sets the specified attachment point of a leader for an annotation with the specified index.
Sets the specified attachment point of a leader for an annotation with the specified index.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetLeaderAttachmentPointAtIndex( _
   ByVal Index As System.Integer, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Boolean
```

```

Dim instance As IAnnotation
Dim Index As System.Integer
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Boolean
 
value = instance.SetLeaderAttachmentPointAtIndex(Index, X, Y, Z)
```

```

System.bool SetLeaderAttachmentPointAtIndex( 
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.bool SetLeaderAttachmentPointAtIndex( 
   System.int Index,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*Index*
:   Index of annotation (see **Remarks**)

*X*
:   x-coordinate of attachment point

*Y*
:   y-coordinate of attachment point

*Z*
:   z-coordinate of attachment point

#### Return Value

True if leader attached successfully, false if not

Remarks

The annotation must be of a type that supports leaders. Only notes, GTols, surface finish symbols, weld symbols, datum target symbols, and block instances support leaders of any kind.

Example

```

'VBA example  
'Open a drawing.  
'Select a view with one note annotation.   
'No other annotations are present.   
'If there are other annotations, modify Index in the   
'method call below to point to the note annotation.  
================================  
Option Explicit  
Dim swApp As SldWorks.SldWorks  
Dim swModel As SldWorks.ModelDoc2  
Dim swDrawing As SldWorks.DrawingDoc  
Dim swAnnot As SldWorks.Annotation  
Dim vAnnotations As Variant  
Dim swView As SldWorks.View  
Dim i As Integer  
Dim bRet As Boolean  
Dim cnt As Long  
Sub main()  
    Set swApp = Application.SldWorks  
    Set swModel = swApp.ActiveDoc  
      
    Set swDrawing = swModel  
    Set swView = swDrawing.ActiveDrawingView  
      
    Debug.Assert Not swView Is Nothing  
    Debug.Print "Name of drawing view: " & swView.GetName2  
      
    vAnnotations = swView.GetAnnotations  
      
    For i = 0 To UBound(vAnnotations)  
        Set swAnnot = vAnnotations(i)  
        swAnnot.Select3 True, Nothing  
      
        cnt = swAnnot.GetLeaderCount  
        If cnt = 1 Then  
            bRet = swAnnot.SetLeaderAttachmentPointAtIndex(0, 0.687021207260901, 0.599975917260352, 250.03275)  
            If (bRet) Then  
                Debug.Print "Leader attached successfully"  
            End If  
        End If  
    Next i  
End Sub
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::SetLeader3 Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~SetLeader3.md)  
[IAnnotation::GetLeaderPointsAtIndex Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderPointsAtIndex.md)  
[IAnnotation::GetLeaderCount Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetLeaderCount.md)
