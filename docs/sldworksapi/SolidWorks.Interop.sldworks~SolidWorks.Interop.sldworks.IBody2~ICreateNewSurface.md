# ICreateNewSurface Method (IBody2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~ICreateNewSurface`

Creates a handle for a new surface to serve as geometry for a face to be added to the body.
Creates a handle for a new surface to serve as geometry for a face to be added to the body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateNewSurface() As Surface
```

```

Dim instance As IBody2
Dim value As Surface
 
value = instance.ICreateNewSurface()
```

```

Surface ICreateNewSurface()
```

```

Surface^ ICreateNewSurface(); 
```

#### Return Value

[ISurface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISurface.md) object

Remarks

This method is the first in a set of related functions that construct a body from trimmed surfaces. Internally, this function also creates a list that SOLIDWORKS uses as a place-holder for trimming curves used to trim the surface to the desired shape.

Any existing object created by this method is destroyed if you call this method again.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)  
[IBody2::CreateNewSurface Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~CreateNewSurface.md)
