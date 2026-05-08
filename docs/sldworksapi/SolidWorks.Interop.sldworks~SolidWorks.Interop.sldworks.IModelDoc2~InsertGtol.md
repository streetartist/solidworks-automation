# InsertGtol Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertGtol`

Creates a new geometric tolerance symbol (GTol) in this document.
Creates a new geometric tolerance symbol (GTol) in this document.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertGtol() As System.Object
```

```

Dim instance As IModelDoc2
Dim value As System.Object
 
value = instance.InsertGtol()
```

```

System.object InsertGtol()
```

```

System.Object^ InsertGtol(); 
```

#### Return Value

Newly created [GTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md)

Remarks

The leader attachment point for the newly created GTol object comes from the selection made before calling this method. The initial location of the symbol is near the selection location. If there is no selection, then the GTol does not have a leader, is free standing, and is initially at the origin of the model or drawing.

This method creates an empty symbol. To fill in the text and symbols of this GTol, use the pointer returned by this method to access the various get and set methods of the [IGTol](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol.md) interface, such as [IGtol::SetFrameSymbols2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameSymbols2.md) and [IGtol::SetFrameValues](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~SetFrameValues.md). Use [IGtol::GetAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IGtol~GetAnnotation.md) to retrieve the [IAnnotation](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md) object.

Example

[Insert GTol (C#)](Insert_GTol_Example_CSharp.htm)  
[Insert GTol (VB.NET)](Insert_GTol_Example_VBNET.htm)  
[Insert GTol (VBA)](Insert_GTol_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::IInsertGtol Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~IInsertGtol.md)
