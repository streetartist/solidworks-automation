# HasLoadBearingFaces Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~HasLoadBearingFaces`

Gets whether this mate has load bearing faces.
Gets whether this mate has load bearing faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property HasLoadBearingFaces As System.Boolean
```

```

Dim instance As IMate2
Dim value As System.Boolean
 
value = instance.HasLoadBearingFaces
```

```

System.bool HasLoadBearingFaces {get;}
```

```

property System.bool HasLoadBearingFaces {
   System.bool get();
}
```

#### Property Value

True if the mate has load bearing faces, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::IsLoadBearingFacesBonded Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IsLoadBearingFacesBonded.md)
