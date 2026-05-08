# SetDisplayMode4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode4`

Sets the display mode of this drawing view.
Sets the display mode of this drawing view.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDisplayMode4( _
   ByVal UseParent As System.Boolean, _
   ByVal Mode As System.Integer, _
   ByVal Faceted As System.Boolean, _
   ByVal Edges As System.Boolean, _
   ByVal CThreadHighQuality As System.Boolean _
) As System.Boolean
```

```

Dim instance As IView
Dim UseParent As System.Boolean
Dim Mode As System.Integer
Dim Faceted As System.Boolean
Dim Edges As System.Boolean
Dim CThreadHighQuality As System.Boolean
Dim value As System.Boolean
 
value = instance.SetDisplayMode4(UseParent, Mode, Faceted, Edges, CThreadHighQuality)
```

```

System.bool SetDisplayMode4( 
   System.bool UseParent,
   System.int Mode,
   System.bool Faceted,
   System.bool Edges,
   System.bool CThreadHighQuality
)
```

```

System.bool SetDisplayMode4( 
   System.bool UseParent,
   System.int Mode,
   System.bool Faceted,
   System.bool Edges,
   System.bool CThreadHighQuality
) 
```

#### Parameters

*UseParent*
:   True to use the parent's settings, false to use this drawing view's local settings (see **Remarks**)

*Mode*
:   Display mode of the drawing view as defined in [swDisplayMode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayMode_e.html) (see **Remarks**)

*Faceted*
:   True for draft quality, false for precision quality (see **Remarks**)

*Edges*
:   True if edges are displayed when this view is in shaded mode, false if not

*CThreadHighQuality*
:   True for precision quality cosmetic threads, false for draft quality

#### Return Value

True if the display mode is reset, false if not

Remarks

If UseParent is true and a parent view:

- Exists, then this method's Mode, Faceted, and Edges parameters are ignored.
- Does not exist, then this method does not change the current display mode of this drawing view.

Mode specifies the drawing view display as defined by swDisplayMode\_e.:

- swWIREFRAME
- swHIDDEN (Hidden Lines Removed)
- swHIDDEN\_GREYED (Hidden Lines Visible)
- swSHADED
- swSHADED\_EDGES

swDisplayMode\_e also contains three other values that seem to indicate faceted (draft) geometry:

- swFACETED\_WIREFRAME
- swFACETED\_HIDDEN\_GREYED
- swFACETED\_HIDDEN

However in this method, you must use the Faceted parameter (not the Mode parameter) to specify draft or precision quality. If you specify Mode with swFACETED\_WIREFRAME, swFACETED\_HIDDEN\_GREYED, or swFACETED\_HIDDEN, then SOLIDWORKS instead uses swWIREFRAME, swHIDDEN\_GREYED, or swHIDDEN.

NOTE: Just as displaying geometry precisely can decrease performance, setting the Faceted argument to true (draft quality) can increase performance.

|  |  |
| --- | --- |
| **To determine for this view...** | **Use...** |
| Whether its edges are displayed when it's in shaded mode | [IView::GetDisplayEdgesInShadedMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayEdgesInShadedMode.md) |
| Whether its geometry is faceted | [IView::GetFacettedHlrDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFacettedHlrDisplay.md) |
| Its current display mode | [IView::GetDisplayMode2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.md) |
| Whether its parent's display mode is being used | [IView::GetUseParentDisplayMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUseParentDisplayMode.md) |
| Its cosmetic thread display quality | [IView::GetCThreadQuality](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetCThreadQuality.md) |

Example

'VBA

'-------------------------------------  
' Preconditions:  
' 1. Open a drawing and select a drawing view.  
' 2. Open the Immediate window.  
'  
' Postconditions:  
' 1. Gets the selected view's current display mode properties.  
' 2. Resets the display mode properties.  
' 3. Gets the new display mode properties.  
' 4. Examine the Immediate window.  
'--------------------------------------

Option Explicit  
Sub main()

    Dim swApp As SldWorks.SldWorks  
    Dim swModel As SldWorks.ModelDoc2  
    Dim swDraw As SldWorks.DrawingDoc  
    Dim swSheet As SldWorks.Sheet  
    Dim swView As SldWorks.View  
    Dim bRet As Boolean  
    Dim swSelectionMgr As SldWorks.SelectionMgr

    Set swApp = SolidWorks.SldWorks  
    Set swModel = swApp.ActiveDoc  
    Set swDraw = swModel  
    Set swSheet = swDraw.GetCurrentSheet  
    Set swSelectionMgr = swModel.SelectionManager  
     
    Set swView = swSelectionMgr.GetSelectedObject6(1, -1)

    Debug.Print "=====Current Display Mode======"  
    Debug.Print ""  
  
    Dim UseParentProp As Boolean  
    UseParentProp = swView.**GetUseParentDisplayMode**  
    Debug.Print "Using parent view's display mode?  " & UseParentProp  
     
    Dim displayMode As Long  
    displayMode = swView.**GetDisplayMode2**  
    Debug.Print "Current display mode as defined by swDisplayMode\_e:  " & displayMode  
     
    Dim Faceted As Boolean  
    Faceted = swView.**GetFacettedHlrDisplay**  
    Debug.Print "Display faceted?:  " & Faceted  
     
    Dim EdgesMode As Boolean  
    EdgesMode = swView.**GetDisplayEdgesInShadedMode**  
    Debug.Print "Display edges when the view is in shaded mode?  " & EdgesMode  
     
     
    Dim cThreadQuality As Boolean  
    cThreadQuality = swView.**GetCThreadQuality**  
    Debug.Print "Precision quality for cosmetic threads? " & swView.GetCThreadQuality  
     
    swView.**SetDisplayMode4** False, 3, True, False, True  
     
    Debug.Print "=====After Re-setting Display Mode======"  
    Debug.Print ""  
    Debug.Print "Using parent view's display mode?  " & swView.**GetUseParentDisplayMode**  
    Debug.Print "Current display mode as defined by swDisplayMode\_e:  " & swView.**GetDisplayMode2**  
    Debug.Print "Display faceted?  " & swView.**GetFacettedHlrDisplay**  
    Debug.Print "Display edges when the view is in shaded mode?  " & swView.**GetDisplayEdgesInShadedMode**  
    Debug.Print "Precision quality for cosmetic threads? " & swView.**GetCThreadQuality**

End Sub

Example

[Set Display Mode of View (VB.NET)](Set_Display_Mode_of_View_Example_VBNET.htm)  
[Set Display Mode of View (C#)](Set_Display_Mode_of_View_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)
