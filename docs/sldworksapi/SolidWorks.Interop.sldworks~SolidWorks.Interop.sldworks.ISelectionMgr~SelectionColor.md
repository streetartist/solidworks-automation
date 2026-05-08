# SelectionColor Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~SelectionColor`

Gets or sets the selection color.
Gets or sets the selection color.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SelectionColor( _
   ByVal Mark As System.Integer _
) As System.Integer
```

```

Dim instance As ISelectionMgr
Dim Mark As System.Integer
Dim value As System.Integer
 
instance.SelectionColor(Mark) = value
 
value = instance.SelectionColor(Mark)
```

```

System.int SelectionColor( 
   System.int Mark
) {get; set;}
```

```

property System.int SelectionColor {
   System.int get(System.int Mark);
   void set (System.int Mark, System.int value);
}
```

#### Parameters

*Mark*
:   Mark value (see **Remarks**)

#### Property Value

Value indicating the color to use for a selection as defined by swSystemColors; these values are from [swUserPreferenceIntegerValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceIntegerValue_e.html)  (see Remarks)

Remarks

You should have a set of marks that you want to apply to selected objects. These marks are application specific and should be designed to present to the user a visual collection of like objects.

The values that SOLIDWORKS internal dialogs typically use for selection colors are:

- swSystemColorsSelectedItem1
- swSystemColorsSelectedItem2
- swSystemColorsSelectedItem3

You can also specify any of the following values:

- swSystemColorsViewportBackground
- swSystemColorsTopGradientColor
- swSystemColorsBottomGradientColor
- swSystemColorsDynamicHighlight
- swSystemColorsHighlight
- swSystemColorsSelectedFaceShaded
- swSystemColorsDrawingsVisibleModelEdge
- swSystemColorsDrawingsHiddenModelEdge

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISelectionMgr Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr.md)  
[ISelectionMgr Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr_members.md)  
[ISelectionMgr::ClearSelectionColors Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISelectionMgr~ClearSelectionColors.md)
