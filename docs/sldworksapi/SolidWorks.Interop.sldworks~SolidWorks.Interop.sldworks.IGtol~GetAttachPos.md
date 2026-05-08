# GetAttachPos Method (IGtol)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAttachPos`

Gets the attachment point of the GTol.
Gets the attachment point of the GTol.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetAttachPos() As System.Object
```

```

Dim instance As IGtol
Dim value As System.Object
 
value = instance.GetAttachPos()
```

```

System.object GetAttachPos()
```

```

System.Object^ GetAttachPos(); 
```

#### Return Value

Array (see **Remarks**)

Remarks

This method is meaningful only if this GTol is attached.

Format of return value is the following array of doubles:

*retval*[0] = X-coordinate of attachment point

*retval*[1] = Y-coordinate of attachment point

*retval*[2] = Z-coordinate of attachment point

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IGtol Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)  
[IGtol Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol_members.md)  
[IGtol::IGetAttachPos Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~IGetAttachPos.md)
