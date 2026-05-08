# BendAllowanceType Property (IBendsFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~BendAllowanceType`

Obsolete. Superseded by IBendsFeatureData::GetCustomBendAllowance and IBendsFeatureData::SetCustomBendAllowance.
Obsolete. Superseded by [IBendsFeatureData::GetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~GetCustomBendAllowance.md) and [IBendsFeatureData::SetCustomBendAllowance](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData~SetCustomBendAllowance.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property BendAllowanceType As System.Integer
```

```

Dim instance As IBendsFeatureData
Dim value As System.Integer
 
instance.BendAllowanceType = value
 
value = instance.BendAllowanceType
```

```

System.int BendAllowanceType {get; set;}
```

```

property System.int BendAllowanceType {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Type of bend allowance as defined in [swBendAllowanceTypes\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swBendAllowanceTypes_e.html)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBendsFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData.md)  
[IBendsFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBendsFeatureData_members.md)
