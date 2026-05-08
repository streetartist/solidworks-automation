# PickPoints Property (IConcentricMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~PickPoints`

Gets or sets the pick points for the entities to mate in this concentric mate.
Gets or sets the pick points for the entities to mate in this concentric mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PickPoints As System.Object
```

```

Dim instance As IConcentricMateFeatureData
Dim value As System.Object
 
instance.PickPoints = value
 
value = instance.PickPoints
```

```

System.object PickPoints {get; set;}
```

```

property System.Object^ PickPoints {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

Array of x, y, z-coordinates, one set for each mate entity

Remarks

After you set the pick points for a given selection of [IConcentricMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData~EntitiesToMate.md), you cannot modify the pick points. If you want to use new pick points, then you must create an entirely new concentric mate.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IConcentricMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData.md)  
[IConcentricMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IConcentricMateFeatureData_members.md)
