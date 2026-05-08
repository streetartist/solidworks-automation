# CreatePlaneAtSurface2 Method (IModelDoc)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc~CreatePlaneAtSurface2`

Obsolete. Superseded by IModelDoc2::CreatePlaneAtSurface2.
Obsolete. Superseded by [IModelDoc2::CreatePlaneAtSurface2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~CreatePlaneAtSurface2.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function CreatePlaneAtSurface2( _
   ByVal InterIndex As System.Integer, _
   ByVal ProjOpt As System.Boolean, _
   ByVal ReverseDir As System.Boolean, _
   ByVal NormalPlane As System.Boolean, _
   ByVal Angle As System.Double _
) As System.Object
```

```

Dim instance As IModelDoc
Dim InterIndex As System.Integer
Dim ProjOpt As System.Boolean
Dim ReverseDir As System.Boolean
Dim NormalPlane As System.Boolean
Dim Angle As System.Double
Dim value As System.Object
 
value = instance.CreatePlaneAtSurface2(InterIndex, ProjOpt, ReverseDir, NormalPlane, Angle)
```

```

System.object CreatePlaneAtSurface2( 
   System.int InterIndex,
   System.bool ProjOpt,
   System.bool ReverseDir,
   System.bool NormalPlane,
   System.double Angle
)
```

```

System.Object^ CreatePlaneAtSurface2( 
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

[IModelDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc.md)  
[IModelDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc_members.md)
