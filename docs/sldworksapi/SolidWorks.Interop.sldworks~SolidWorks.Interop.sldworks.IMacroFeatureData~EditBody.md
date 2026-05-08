# EditBody Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBody`

Obsolete. Superseded by IMacroFeatureData::IGetEditBodies, IMacroFeatureData::ISetEditBodies, and IMacroFeatureData::EditBodies.
Obsolete. Superseded by [IMacroFeatureData::IGetEditBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~IGetEditBodies.md), [IMacroFeatureData::ISetEditBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~ISetEditBodies.md), and [IMacroFeatureData::EditBodies](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData~EditBodies.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property EditBody As Body2
```

```

Dim instance As IMacroFeatureData
Dim value As Body2
 
instance.EditBody = value
 
value = instance.EditBody
```

```

Body2 EditBody {get; set;}
```

```

property Body2^ EditBody {
   Body2^ get();
   void set (    Body2^ value);
}
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMacroFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData.md)  
[IMacroFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMacroFeatureData_members.md)
