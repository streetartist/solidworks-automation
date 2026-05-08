# NumberOfPlanes Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~NumberOfPlanes`

Gets or sets the number of slicing planes.
Gets or sets the number of slicing planes.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property NumberOfPlanes As System.Integer
```

```

Dim instance As ISlicingData
Dim value As System.Integer
 
instance.NumberOfPlanes = value
 
value = instance.NumberOfPlanes
```

```

System.int NumberOfPlanes {get; set;}
```

```

property System.int NumberOfPlanes {
   System.int get();
   void set (    System.int value);
}
```

#### Property Value

Number of slicing planes

Remarks

The number of slicing planes cannot exceed 100.

Example

See the [ISlicingData](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md) example.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISlicingData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData.md)  
[ISlicingData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData_members.md)  
[ISlicingData::PlaneReferences Property ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISlicingData~PlaneReferences.md)
