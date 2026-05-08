# AllowExtension Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData~AllowExtension`

Gets and sets whether to extend structural members.
Gets and sets whether to extend structural members.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property AllowExtension As System.Boolean
```

```

Dim instance As ICornerTreatmentFeatureData
Dim value As System.Boolean
 
instance.AllowExtension = value
 
value = instance.AllowExtension
```

```

System.bool AllowExtension {get; set;}
```

```

property System.bool AllowExtension {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to extend structural members, false to not

Example

See the [ICornerManagementFolder](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerManagementFolder.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICornerTreatmentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData.md)  
[ICornerTreatmentFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICornerTreatmentFeatureData_members.md)
