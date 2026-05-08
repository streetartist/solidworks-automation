# IEdgeGetFace Method (IMidSurface)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface~IEdgeGetFace`

Obsolete. Superseded by IMidSurface2::IEdgeGetFace.
Obsolete. Superseded by [IMidSurface2::IEdgeGetFace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface2~IEdgeGetFace.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IEdgeGetFace( _
   ByVal EdgeInDisp As Edge _
) As Face
```

```

Dim instance As IMidSurface
Dim EdgeInDisp As Edge
Dim value As Face
 
value = instance.IEdgeGetFace(EdgeInDisp)
```

```

Face IEdgeGetFace( 
   Edge EdgeInDisp
)
```

```

Face^ IEdgeGetFace( 
   Edge^ EdgeInDisp
) 
```

#### Parameters

*EdgeInDisp*

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMidSurface Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface.md)  
[IMidSurface Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMidSurface_members.md)
