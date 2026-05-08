# SetSelectionColor Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox~SetSelectionColor`

Sets the color for selections made in this selection box on the PropertyManager page.
Sets the color for selections made in this selection box on the PropertyManager page.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function SetSelectionColor( _
   ByVal Special As System.Boolean, _
   ByVal Color As System.Integer _
) As System.Boolean
```

```

Dim instance As IPropertyManagerPageSelectionbox
Dim Special As System.Boolean
Dim Color As System.Integer
Dim value As System.Boolean
 
value = instance.SetSelectionColor(Special, Color)
```

```

System.bool SetSelectionColor( 
   System.bool Special,
   System.int Color
)
```

```

System.bool SetSelectionColor( 
   System.bool Special,
   System.int Color
) 
```

#### Parameters

*Special*
:   True uses a specific color for selections, false does not

*Color*
:   Color to use for selections as defined by the swSystemColors; values from [swUserPreferenceIntegerValue\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swUserPreferenceIntegerValue_e.html)  (see **Remarks**)

Remarks

You can only use this method to set properties on the PropertyManager page before it is displayed or while it is closed. See [IPropertyManagerPage2::Show2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Show2.md) and [IPropertyManagerPage2::Close](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPage2~Close.md).

By default, the selection box created uses the default selection color. You can use this method to override that default behavior. When you specify a specific selection color by setting the Special argument to True and specifying a color in the Color argument, the resulting selection box has a narrow color bar next to the selection box that is the same color as any faces selected in the graphics area.

The colors that SOLIDWORKS internal dialogs typically use for selection colors are:

- swSystemColorsSelectedItem1
- swSystemColorsSelectedItem2
- swSystemColorsSelectedItem3

Although you should use the typical selection colors for a consistent look-and-feel among your PropertyManager and SOLIDWORKS PropertyManager pages, you can specify any of the following values:

- swSystemColorsViewportBackground
- swSystemColorsTopGradientColor
- swSystemColorsBottomGradientColor
- swSystemColorsDynamicHighlight
- swSystemColorsHighlight
- swSystemColorsSelectedFaceShaded
- swSystemColorsDrawingsVisibleModelEdge
- swSystemColorsDrawingsHiddenModelEdge
- swSystemColorsDrawingsPaperBorder
- swSystemColorsDrawingsPaperShadow
- swSystemColorsImportedDrivingAnnotation
- swSystemColorsImportedDrivenAnnotation
- swSystemColorsSketchOverDefined
- swSystemColorsSketchFullyDefined
- swSystemColorsSketchUnderDefined
- swSystemColorsSketchInvalidGeometry
- swSystemColorsSketchNotSolved
- swSystemColorsGridLinesMinor
- swSystemColorsGridLinesMajor
- swSystemColorsConstructionGeometry
- swSystemColorsDanglingDimension
- swSystemColorsText
- swSystemColorsAssemblyEditPart
- swSystemColorsAssemblyEditPartHiddenLines
- swSystemColorsAssemblyNonEditPart
- swSystemColorsInactiveEntity
- swSystemColorsTemporaryGraphics
- swSystemColorsTemporaryGraphicsShaded
- swSystemColorsActiveSelectionListBox
- swSystemColorsSurfacesOpenEdge
- swSystemColorsTreeViewBackground
- swSystemColorsShadedEdge

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPropertyManagerPageSelectionbox Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox.md)  
[IPropertyManagerPageSelectionbox Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPropertyManagerPageSelectionbox_members.md)
