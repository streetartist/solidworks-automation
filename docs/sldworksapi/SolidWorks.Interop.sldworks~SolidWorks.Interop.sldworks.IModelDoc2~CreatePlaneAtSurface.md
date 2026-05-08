# CreatePlaneAtSurface Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtSurface`

Obsolete. Superseded by IModelDoc2::CreatePlaneAtSurface3.
Obsolete. Superseded by [IModelDoc2::CreatePlaneAtSurface3](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ICreatePlaneAtSurface3.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Sub CreatePlaneAtSurface( _
   ByVal InterIndex As System.Integer, _
   ByVal ProjOpt As System.Boolean, _
   ByVal ReverseDir As System.Boolean, _
   ByVal NormalPlane As System.Boolean, _
   ByVal Angle As System.Double _
) 
```

```

Dim instance As IModelDoc2
Dim InterIndex As System.Integer
Dim ProjOpt As System.Boolean
Dim ReverseDir As System.Boolean
Dim NormalPlane As System.Boolean
Dim Angle As System.Double
 
instance.CreatePlaneAtSurface(InterIndex, ProjOpt, ReverseDir, NormalPlane, Angle)
```

```

void CreatePlaneAtSurface( 
   System.int InterIndex,
   System.bool ProjOpt,
   System.bool ReverseDir,
   System.bool NormalPlane,
   System.double Angle
)
```

```

void CreatePlaneAtSurface( 
   System.int InterIndex,
   System.bool ProjOpt,
   System.bool ReverseDir,
   System.bool NormalPlane,
   System.double Angle
) 
```

#### Parameters

*InterIndex*

*ProjOpt*

*ReverseDir*

*NormalPlane*

*Angle*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
