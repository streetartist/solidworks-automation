# PickPoints Property (ICoincidentMateFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~PickPoints`

Gets or sets the pick points for the entities to mate in this coincident mate.
Gets or sets the pick points for the entities to mate in this coincident mate.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property PickPoints As System.Object
```

```

Dim instance As ICoincidentMateFeatureData
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

Array of x, y, z-coordinates, one set for each mate entity in [ICoincidentMateFeatureData::EntitiesToMate](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData~EntitiesToMate.md)

Remarks

Pick points define the position of the entities to mate. If no pick points are specified, then entities are mated using default pick points.

After you create this mate using the pick points for a given selection of ICoincidentMateFeatureData::EntitiesToMate, you cannot edit the pick points. If you want to use new pick points, then you must create an entirely new coincident mate with mate entities and pick points.

If you pre-select the mate entities by coordinates (e.g., [IModelDocExtension::SelectByID2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~SelectByID2.md)), then you do not need to specify pick points.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ICoincidentMateFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData.md)  
[ICoincidentMateFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ICoincidentMateFeatureData_members.md)
