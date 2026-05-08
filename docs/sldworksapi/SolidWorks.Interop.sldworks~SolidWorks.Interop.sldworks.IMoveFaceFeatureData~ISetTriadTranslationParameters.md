# ISetTriadTranslationParameters Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~ISetTriadTranslationParameters`

Sets the translation parameters for this Move Face feature.
Sets the translation parameters for this Move Face feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub ISetTriadTranslationParameters( _
   ByRef TranslationParameters As System.Double _
) 
```

```

Dim instance As IMoveFaceFeatureData
Dim TranslationParameters As System.Double
 
instance.ISetTriadTranslationParameters(TranslationParameters)
```

```

void ISetTriadTranslationParameters( 
   ref System.double TranslationParameters
)
```

```

void ISetTriadTranslationParameters( 
   System.double% TranslationParameters
) 
```

#### Parameters

*TranslationParameters*
:   - in-process, unmanaged C++: pointer to an array of three doubles for the X, Y, and Z translation parameters
    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_methods.htm) for details about this type of method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMoveFaceFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData.md)  
[IMoveFaceFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData_members.md)  
[IMoveFaceFeatureData::IGetTriadTranslationParameters Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~IGetTriadTranslationParameters.md)  
[IMoveFaceFeatureData::TriadTranslationParameters Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMoveFaceFeatureData~TriadTranslationParameters.md)
