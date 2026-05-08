# Provider Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~Provider`

Gets or sets the error message to display in the What's Wrong dialog when a non-embedded macro feature fails to rebuild due to missing files.
Gets or sets the error message to display in the What's Wrong dialog when a non-embedded macro feature fails to rebuild due to missing files.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Provider As System.String
```

```

Dim instance As IMacroFeatureData
Dim value As System.String
 
instance.Provider = value
 
value = instance.Provider
```

```

System.string Provider {get; set;}
```

```

property System.String^ Provider {
   System.String^ get();
   void set (    System.String^ value);
}
```

#### Property Value

Error message

Remarks

This property allows you to replace the generic error message that appears in the What's Wrong dialog with a more detailed error message when this non-embedded macro feature fails to load or rebuild due to missing files.

Possible causes of macro feature rebuild failure:

- The model contains this COM-based macro feature, but the rebuild, edit, and security callbacks exist in an add-in that SOLIDWORKS cannot locate.
- The model references this non-embedded macro feature which exists in a VBA macro that SOLIDWORKS cannot locate.
- Third-party DLLs, add-in files, or other files associated with this non-embedded macro feature are missing.

**NOTE:** All files required by embedded macro features are serialized with the model, so **File not found** errors do not occur for embedded macros, and this property need not be set for them.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)  
[IMacroFeatureData::EmbedMacroFile Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EmbedMacroFile.md)  
[IMacroFeatureData::MacroFileEmbedded Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~MacroFileEmbedded.md)  
[IModelDocExtension::GetWhatsWrong Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetWhatsWrong.md)
