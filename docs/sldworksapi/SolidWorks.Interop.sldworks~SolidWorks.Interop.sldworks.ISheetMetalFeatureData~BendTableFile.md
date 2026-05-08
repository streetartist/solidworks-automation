# BendTableFile Property (ISheetMetalFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~BendTableFile`

Obsolete. Superseded by ISheetMetalFeatureData::GetCustomBendAllowance and ISheetMetalFeatureData::SetCustomBendAllowance.
Obsolete. Superseded by [ISheetMetalFeatureData::GetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~GetCustomBendAllowance.md) and [ISheetMetalFeatureData::SetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData~SetCustomBendAllowance.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BendTableFile As System.String
```

```

Dim instance As ISheetMetalFeatureData
Dim value As System.String
 
instance.BendTableFile = value
 
value = instance.BendTableFile
```

```

System.string BendTableFile {get; set;}
```

```

property System.String^ BendTableFile {
   System.String^ get();
   void set (    System.String^ value);
}
```

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISheetMetalFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData.md)  
[ISheetMetalFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISheetMetalFeatureData_members.md)
