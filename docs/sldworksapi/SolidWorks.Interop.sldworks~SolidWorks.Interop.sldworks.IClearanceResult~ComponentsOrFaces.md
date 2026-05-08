# ComponentsOrFaces Property

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult~ComponentsOrFaces`

Gets the assembly components, faces, or both involved in this clearance result.
Gets the assembly components, faces, or both involved in this clearance result.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

ReadOnly Property ComponentsOrFaces As System.Object
```

```

Dim instance As IClearanceResult
Dim value As System.Object
 
value = instance.ComponentsOrFaces
```

```

System.object ComponentsOrFaces {get;}
```

```

property System.Object^ ComponentsOrFaces {
   System.Object^ get();
}
```

#### Property Value

Array of assembly [component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)s, [face](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)s, or both

Example

See the [IClearanceVerificationMgr](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceVerificationMgr.md) examples.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IClearanceResult Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult.md)  
[IClearanceResult Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IClearanceResult_members.md)
