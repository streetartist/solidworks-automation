# Offset Property (ISlicingData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~Offset`

Gets or sets the linear or radial spacing between slicing planes.
Gets or sets the linear or radial spacing between slicing planes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property Offset As System.Double
```

```

Dim instance As ISlicingData
Dim value As System.Double
 
instance.Offset = value
 
value = instance.Offset
```

```

System.double Offset {get; set;}
```

```

property System.double Offset {
   System.double get();
   void set (    System.double value);
}
```

#### Property Value

Linear spacing (meters) or radial spacing (radians) between slicing planes (see **Remarks**)

Remarks

If [ISlicingData::PlaneReferences](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~PlaneReferences.md) specifies:

- a planar entity, then this property specifies linear spacing between slices.
- a linear entity and a point entity, then this property specifies radial spacing between slices.

Example

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md)  
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.md)
