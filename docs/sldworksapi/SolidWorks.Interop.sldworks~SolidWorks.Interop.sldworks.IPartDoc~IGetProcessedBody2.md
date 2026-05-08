# IGetProcessedBody2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetProcessedBody2`

Pre-processes the geometry of a body so that:
Pre-processes the geometry of a body so that:

- Closed periodic faces (for example, the lateral face of a cylinder) are split into two faces.
- Faces that straddle the seam, if any, of the underlying surface are split into two faces.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetProcessedBody2() As Body2
```

```

Dim instance As IPartDoc
Dim value As Body2
 
value = instance.IGetProcessedBody2()
```

```

Body2 IGetProcessedBody2()
```

```

Body2^ IGetProcessedBody2(); 
```

#### Return Value

Processed [body](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md), which is a copy of the body for this part

Remarks

Preprocessing is sometimes necessary (for example, IGES files), for exporting to systems that have difficulty with periodic conditions.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IPartDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc.md)  
[IPartDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc_members.md)  
[IBody2::GetProcessedBody2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBody2.md)  
[IBody2::GetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~GetProcessedBodyWithSelFace.md)  
[IBody2::IGetProcessedBodyWithSelFace Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBodyWithSelFace.md)  
[IPartDoc::IGetProcessedBodyWithSelFace2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IPartDoc~IGetProcessedBodyWithSelFace2.md)  
[IBody2::IGetProcessedBody Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~IGetProcessedBody.md)
