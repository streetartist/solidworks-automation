# GetAdvancedSaveAsOptions Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetAdvancedSaveAsOptions`

Gets the advanced File &gt; Save As options.
Gets the advanced **File > Save As** options.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAdvancedSaveAsOptions( _
   ByVal Options As System.Integer _
) As System.Object
```

```

Dim instance As IModelDocExtension
Dim Options As System.Integer
Dim value As System.Object
 
value = instance.GetAdvancedSaveAsOptions(Options)
```

```

System.object GetAdvancedSaveAsOptions( 
   System.int Options
)
```

```

System.Object^ GetAdvancedSaveAsOptions( 
   System.int Options
) 
```

#### Parameters

*Options*
:   Save with references options as defined in [swSaveWithReferencesOptions](ms-help://SolidWorks.Interop.swconst/SolidWorks/SolidWorks.Interop.swconst~SolidWorks.Interop.swconst.swSaveWithReferencesOptions_e.html) (see **Remarks**)

#### Return Value

[IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md)

Remarks

Call this method before calling [IModelDocExtension::SaveAs3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SaveAs3.md).

[IAdvancedSaveAsOptions::GetItemsNameAndPath](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions~GetItemsNameAndPath.md) returns a list of items according to how the Options parameter is specified in this method.

Example

See the [IAdvancedSaveAsOptions](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAdvancedSaveAsOptions.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDocExtension Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension.md)  
[IModelDocExtension Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension_members.md)
