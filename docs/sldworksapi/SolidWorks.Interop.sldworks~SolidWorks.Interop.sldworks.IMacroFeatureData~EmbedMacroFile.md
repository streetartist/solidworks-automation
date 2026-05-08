# EmbedMacroFile Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EmbedMacroFile`

Sets whether to embed the macro file in the model with the macro feature.
Sets whether to embed the macro file in the model with the macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function EmbedMacroFile() As System.Boolean
```

```

Dim instance As IMacroFeatureData
Dim value As System.Boolean
 
value = instance.EmbedMacroFile()
```

```

System.bool EmbedMacroFile()
```

```

System.bool EmbedMacroFile(); 
```

#### Return Value

True to embed the macro file in the model with the macro feature, false to not

Remarks

Call [IMacroFeatureData::MacroFileEmbedded](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~MacroFileEmbedded.md) to determine if the macro file is embedded with the macro feature.

If this property is set to false, you should specify a detailed error message to display in the What's Wrong dialog when SOLIDWORKS fails to find files during macro feature load or rebuild. Specify this error message using [IMacroFeatureData:Provider](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Provider.md).

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)
