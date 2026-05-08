# ReferenceComponent1 Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData~ReferenceComponent1`

Gets or sets the reference component of the first mate entity of this linear coupler mate.
Gets or sets the reference component of the first mate entity of this linear coupler mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ReferenceComponent1 As System.Object
```

```

Dim instance As ILinearCouplerMateFeatureData
Dim value As System.Object
 
instance.ReferenceComponent1 = value
 
value = instance.ReferenceComponent1
```

```

System.object ReferenceComponent1 {get; set;}
```

```

property System.Object^ ReferenceComponent1 {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Reference component 1

Remarks

Use this property to set up the motion of the first mated component with respect to a reference component. If you do not set this property, motion is with respect to the assembly origin.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ILinearCouplerMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData.md)  
[ILinearCouplerMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ILinearCouplerMateFeatureData_members.md)
