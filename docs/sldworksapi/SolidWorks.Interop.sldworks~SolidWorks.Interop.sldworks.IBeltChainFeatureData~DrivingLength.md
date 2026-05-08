# DrivingLength Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~DrivingLength`

Gets and sets whether belt length can be changed.
Gets and sets whether belt length can be changed.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property DrivingLength As System.Boolean
```

```

Dim instance As IBeltChainFeatureData
Dim value As System.Boolean
 
instance.DrivingLength = value
 
value = instance.DrivingLength
```

```

System.bool DrivingLength {get; set;}
```

```

property System.bool DrivingLength {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to allow belt length changes, false to not

Remarks

If this property is true, then use [IBeltChainFeatureData::BeltLength](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~BeltLength.md) to set the belt length. Pulley positions adjust if at least one pulley has an appropriate degree of freedom.

Example

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)
