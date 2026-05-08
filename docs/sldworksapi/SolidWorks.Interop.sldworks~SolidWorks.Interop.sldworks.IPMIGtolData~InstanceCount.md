# InstanceCount Property (IPMIGtolData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData~InstanceCount`

Gets the number of times this PMI Gtol is repeated.
Gets the number of times this PMI Gtol is repeated.

**NOTE:** **This property is a get-only property.** **Set is not implemented**.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property InstanceCount As System.Integer
```

```

Dim instance As IPMIGtolData
Dim value As System.Integer
 
instance.InstanceCount = value
 
value = instance.InstanceCount
```

```

System.int InstanceCount {get; set;}
```

```

property System.int InstanceCount {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of repeated instances of this Gtol

Example

See the [IAnnotation::GetPMIData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetPMIData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPMIGtolData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData.md)  
[IPMIGtolData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPMIGtolData_members.md)
