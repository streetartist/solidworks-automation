# ProfileLocation Property (IThreadFeatureData)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData~ProfileLocation`

Gets or sets the point or vertex where to start the helix on the thread profile sketch of this thread feature.
Gets or sets the point or vertex where to start the helix on the thread profile sketch of this thread feature.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Property ProfileLocation As System.Object
```

```

Dim instance As IThreadFeatureData
Dim value As System.Object
 
instance.ProfileLocation = value
 
value = instance.ProfileLocation
```

```

System.object ProfileLocation {get; set;}
```

```

property System.Object^ ProfileLocation {
   System.Object^ get();
   void set (    System.Object^ value);
}
```

#### Property Value

[Point](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IRefPoint.md) or [vertex](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IVertex.md) in the thread profile sketch where to start the thread helix

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IThreadFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData.md)  
[IThreadFeatureData Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IThreadFeatureData_members.md)
