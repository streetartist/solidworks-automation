# IsLoadBearingFacesBonded Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~IsLoadBearingFacesBonded`

Get whether the load bearing faces of this mate are bonded.
Get whether the load bearing faces of this mate are bonded.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property IsLoadBearingFacesBonded As System.Boolean
```

```

Dim instance As IMate2
Dim value As System.Boolean
 
value = instance.IsLoadBearingFacesBonded
```

```

System.bool IsLoadBearingFacesBonded {get;}
```

```

property System.bool IsLoadBearingFacesBonded {
   System.bool get();
}
```

#### Property Value

True if the load-bearing faces of this mate are bonded, false if not

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMate2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2.md)  
[IMate2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2_members.md)  
[IMate2::HasLoadBearingFaces Property](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMate2~HasLoadBearingFaces.md)
