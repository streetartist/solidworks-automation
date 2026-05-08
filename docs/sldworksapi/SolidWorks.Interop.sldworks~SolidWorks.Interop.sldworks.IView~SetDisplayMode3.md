# SetDisplayMode3 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode3`

Obsolete. Superseded by IView::SetDisplayMode4.
Obsolete. Superseded by [IView::SetDisplayMode4](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayMode4.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetDisplayMode3( _
   ByVal UseParent As System.Boolean, _
   ByVal Mode As System.Integer, _
   ByVal Facetted As System.Boolean, _
   ByVal Edges As System.Boolean _
) As System.Boolean
```

```

Dim instance As IView
Dim UseParent As System.Boolean
Dim Mode As System.Integer
Dim Facetted As System.Boolean
Dim Edges As System.Boolean
Dim value As System.Boolean
 
value = instance.SetDisplayMode3(UseParent, Mode, Facetted, Edges)
```

```

System.bool SetDisplayMode3( 
   System.bool UseParent,
   System.int Mode,
   System.bool Facetted,
   System.bool Edges
)
```

```

System.bool SetDisplayMode3( 
   System.bool UseParent,
   System.int Mode,
   System.bool Facetted,
   System.bool Edges
) 
```

#### Parameters

*UseParent*
:   True to use the parent's setting, false to use its own local settings

*Mode*
:   Display mode of the drawing view as defined in [swDisplayMode\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swDisplayMode_e.html)

*Facetted*
:   True if the geometry is displayed with draft quality, false if it is displayed with precision quality (see Remarks)

*Edges*
:   True if edges are displayed when this view is in shaded mode, false if not

#### Return Value

True if the setting of the display mode was successful, false if not

Remarks

The contents of a drawing view can be displayed in different modes, including Wireframe, HLR (Hidden Lines Removed), and HLV (Hidden Lines Visible), and Shaded. This is what the Mode argument indicates, and these values are contained in swDisplayMode\_e. To display a drawing view shaded with edges, set swDrawingsDefaultDisplayTypeHLREdgesWhenShaded to True and set Mode to swSHADED.

This enumeration also contains three other values, swFACETED\_WIREFRAME, swFACETED\_HIDDEN\_GREY, and swFACETEDHIDDEN, which indicate faceted display of geometry. However, in this method, the Facetted argument is how faceted display is indicated, and if any of those three values are used in the Mode argument, they are treated the same as swWIREFRAME, sw\_HIDDEN\_GREY, and sw\_HIDDEN, respectively.

|  |  |
| --- | --- |
| **To determine if...** | **Then use...** |
| Edges are displayed when this view is in shaded mode | [IView::GetDisplayEdgesInShadedMode](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayEdgesInShadedMode.md) |
| This view is displayed with faceted geometry | [IView::GetFacettedHlrDisplay](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetFacettedHlrDisplay.md) |
| The display mode of this drawing view | [IView::GetDisplayMode2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetDisplayMode2.md) |

Although you cannot switch a drawing view from precision quality to draft quality, the geometry can still be displayed in draft quality if that is how your user preferences indicate new drawings views should be created. Once the drawing view has precision quality, whether you created it that way or changed it to that after its creation, you cannot change it to draft quality.

NOTE:  Displaying geometry precisely can increase display quality, but can decrease performance. Setting the Facetted argument to True can increase performance, but can decrease display quality.

Example

[Set View Display Mode (C++)](Set_View_Display_Mode_Example_CPlusPlus_COM.htm)  
[Change Display Mode to Draft Quality (VBA)](Change_Display_Mode_to_Draft_Quality_Example_VB.htm)  
[Get Number of Polylines in Shaded Mode Drawing View (VBA)](Get_Number_of_Polylines_in_Shaded_Mode_Drawing_View_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IView Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView.md)  
[IView Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView_members.md)  
[IView::UpdateViewDisplayGeometry Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~UpdateViewDisplayGeometry.md)  
[IView::SetDisplayTangentEdges2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~SetDisplayTangentEdges2.md)  
[IView::GetUseParentDisplayMode Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IView~GetUseParentDisplayMode.md)
