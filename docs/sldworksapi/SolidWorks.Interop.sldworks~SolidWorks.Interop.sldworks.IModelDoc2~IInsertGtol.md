# IInsertGtol Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertGtol`

Creates a new geometric tolerance symbol (GTol) in this document.
Creates a new geometric tolerance symbol (GTol) in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IInsertGtol() As Gtol
```

```

Dim instance As IModelDoc2
Dim value As Gtol
 
value = instance.IInsertGtol()
```

```

Gtol IInsertGtol()
```

```

Gtol^ IInsertGtol(); 
```

#### Return Value

Newly created [GTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)

Remarks

The leader attachment points for the newly created GTol object come from the selections made before calling this method. The initial location of the symbol is near the selection location. If there are no selections, then the GTol does not have a leader, is free standing, and is initially at the origin of the model or drawing.

This method creates an empty symbol. To fill in the text and symbols of this GTol, use the pointer  returned by this method to access the various get and set methods of the [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md) interface, such as [IGtol::SetFrameSymbols2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.md) and [IGtol::SetFrameValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues.md). Use [IGtol::GetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAnnotation.md) to retrieve the [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertGtol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertGtol.md)
