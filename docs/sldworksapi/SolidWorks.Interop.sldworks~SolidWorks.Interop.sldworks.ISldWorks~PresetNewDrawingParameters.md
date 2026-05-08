# PresetNewDrawingParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~PresetNewDrawingParameters`

Presets the drawing template and sheet size parameters to avoid showing the Sheet Format/Size dialog when creating a new drawing document in the user-interface.
Presets the drawing template and sheet size parameters to avoid showing the Sheet Format/Size dialog when creating a new drawing document in the user-interface.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function PresetNewDrawingParameters( _
   ByVal DrawingTemplate As System.String, _
   ByVal ShowTemplate As System.Boolean, _
   ByVal Width As System.Double, _
   ByVal Height As System.Double _
) As System.Boolean
```

```

Dim instance As ISldWorks
Dim DrawingTemplate As System.String
Dim ShowTemplate As System.Boolean
Dim Width As System.Double
Dim Height As System.Double
Dim value As System.Boolean
 
value = instance.PresetNewDrawingParameters(DrawingTemplate, ShowTemplate, Width, Height)
```

```

System.bool PresetNewDrawingParameters( 
   System.string DrawingTemplate,
   System.bool ShowTemplate,
   System.double Width,
   System.double Height
)
```

```

System.bool PresetNewDrawingParameters( 
   System.String^ DrawingTemplate,
   System.bool ShowTemplate,
   System.double Width,
   System.double Height
) 
```

#### Parameters

*DrawingTemplate*
:   Path and filename (.slddrt) of the drawing template to use

*ShowTemplate*
:   True to show the sheet format, false to not

    **NOTE:** Valid only for standard sheet sizes and when Width and Height are set to 0.

*Width*
:   Width of the drawing sheet

*Height*
:   Height of the drawing sheet

#### Return Value

True if the specified drawing template and sheet size parameters are set, false if not

Remarks

To show the Sheet Format/Size dialog the next time a new drawing document is opened (SOLIDWORKS default behavior), call [ISldWorks::ResetPresetDrawingParameters](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~ResetPresetDrawingParameters.md) after calling this method and opening a new drawing document.

Example

[Preset and Reset Template and Sheet Parameters for New Drawing Documents (VBA)](Preset_and_Reset_Template_and_Sheet_Parameters_for_New_Drawing_Documents_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISldWorks Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks.md)  
[ISldWorks Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks_members.md)
