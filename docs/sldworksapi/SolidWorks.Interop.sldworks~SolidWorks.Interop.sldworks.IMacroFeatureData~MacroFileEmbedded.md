# MacroFileEmbedded Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~MacroFileEmbedded`

Gets whether the macro file is embedded ini the model with the macro feature.
Gets whether the macro file is embedded ini the model with the macro feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property MacroFileEmbedded As System.Boolean
```

```

Dim instance As IMacroFeatureData
Dim value As System.Boolean
 
value = instance.MacroFileEmbedded
```

```

System.bool MacroFileEmbedded {get;}
```

```

property System.bool MacroFileEmbedded {
   System.bool get();
}
```

#### Property Value

True if the macro file is embedded in the model with the macro feature, false if not

Remarks

If this property is false, you should specify a detailed error message to display in the What's Wrong dialog when SOLIDWORKS fails to find files during macro feature load or rebuild. To specify this error message, use [IMacroFeatureData:Provider](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Provider.md).

Call [IMacroFeatureData::EmbedMacroFile](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EmbedMacroFile.md) to set whether to embed the macro file with the macro feature.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)
