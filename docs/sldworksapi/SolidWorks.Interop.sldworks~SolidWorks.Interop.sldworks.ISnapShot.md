# ISnapShot Interface

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot`

Allows access to the snapshot of the graphics area of an assembly opened in Large Design Review mode.
Allows access to the snapshot of the graphics area of an assembly opened in Large Design Review mode.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Public Interface ISnapShot 
```

```

Dim instance As ISnapShot
```

```

public interface ISnapShot 
```

```

public interface class ISnapShot 
```

Remarks

To open an assembly in Large Design Review mode:

1. Call [ISldWorks::GetOpenDocSpec](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~GetOpenDocSpec.md) to create an instance of [IDocumentSpecification](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification.md).
2. Set [IDocumentSpecification::ViewOnly](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDocumentSpecification~ViewOnly.md) to true.
3. Call [ISldWorks::OpenDoc7](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc7.md), passing it the instance of IDocumentSpecification.

- or -  
  
Call [ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md) with the Options parameter set to swOpenDocOptions\_e.swOpenDocOptions\_ViewOnly.

Example

[Open Assembly in Large Design Review Mode (VBA)](Open_Assembly_in_Large_Design_Review_Mode_Example_VB.htm)  
[Open Assembly in Large Design Review Mode (VB.NET)](Open_Assembly_in_Large_Design_Review_Mode_Example_VBNET.htm)  
[Open Assembly in Large Design Review Mode (C#)](Open_Assembly_in_Large_Design_Review_Mode_Example_CSharp.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[ISnapShot Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISnapShot_members.md)  
[SolidWorks.Interop.sldworks Namespace](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks_namespace.md)
