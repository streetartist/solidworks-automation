# CreateBeltPart Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~CreateBeltPart`

Gets and sets whether to create a new part that contains the belt sketch.
Gets and sets whether to create a new part that contains the belt sketch.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property CreateBeltPart As System.Boolean
```

```

Dim instance As IBeltChainFeatureData
Dim value As System.Boolean
 
instance.CreateBeltPart = value
 
value = instance.CreateBeltPart
```

```

System.bool CreateBeltPart {get; set;}
```

```

property System.bool CreateBeltPart {
   System.bool get();
   void set (    System.bool value);
}
```

#### Property Value

True to create a belt part, false to not

Remarks

If this property is set to true, use [IBeltChainFeatureData::AccessBeltPart](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData~AccessBeltPart.md) to get the belt part.

Example

See the [IBeltChainFeatureData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBeltChainFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData.md)  
[IBeltChainFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBeltChainFeatureData_members.md)
