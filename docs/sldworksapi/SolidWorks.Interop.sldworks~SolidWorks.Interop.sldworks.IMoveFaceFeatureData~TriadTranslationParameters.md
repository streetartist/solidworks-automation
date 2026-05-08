# TriadTranslationParameters Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~TriadTranslationParameters`

Gets or sets the translation parameters for this Move Face feature.
Gets or sets the translation parameters for this Move Face feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property TriadTranslationParameters As System.Object
```

```

Dim instance As IMoveFaceFeatureData
Dim value As System.Object
 
instance.TriadTranslationParameters = value
 
value = instance.TriadTranslationParameters
```

```

System.object TriadTranslationParameters {get; set;}
```

```

property System.Object^ TriadTranslationParameters {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of three doubles, which are the X, Y, and Z translation parameters

Example

[Translate Move Face Feature (VB.NET)](Translate_Move_Face_Feature_Example_VBNET.htm)  
[Translate Move Face Feature (VBA)](Translate_Move_Face_Feature_Example_VB.htm)  
[Translate Move Face Feature (C#)](Translate_Move_Face_Feature_Example_CSharp.htm)  
[Create and Modify Move Face Feature (C#)](Create_and_Modify_Move_Face_Feature_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)  
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.md)  
[IMoveFaceFeatureData::IGetTriadTranslationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetTriadTranslationParameters.md)  
[IMoveFaceFeatureData::ISetTriadTranslationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetTriadTranslationParameters.md)
