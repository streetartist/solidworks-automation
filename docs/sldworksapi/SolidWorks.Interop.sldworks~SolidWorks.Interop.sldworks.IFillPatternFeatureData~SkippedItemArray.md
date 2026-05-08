# SkippedItemArray Property (IFillPatternFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData~SkippedItemArray`

Gets or sets the pattern instances to skip in this fill pattern feature.
Gets or sets the pattern instances to skip in this fill pattern feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property SkippedItemArray As System.Object
```

```

Dim instance As IFillPatternFeatureData
Dim value As System.Object
 
instance.SkippedItemArray = value
 
value = instance.SkippedItemArray
```

```

System.object SkippedItemArray {get; set;}
```

```

property System.Object^ SkippedItemArray {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of pattern instances to skip (see **Remarks**)

Remarks

The array is linear and zero-based and contains the (row\_id, column\_id) of each pattern instance to skip.

For example,

> [row\_id\_instance1, column\_id\_instance1, row\_id\_instance2, column\_id\_instance2, ...]

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IFillPatternFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData.md)  
[IFillPatternFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFillPatternFeatureData_members.md)
