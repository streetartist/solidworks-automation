# GetFaces Method (IMateLoadReference)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~GetFaces`

Gets the supplemental faces of the mate associated with the specified component.
Gets the supplemental faces of the mate associated with the specified component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFaces( _
   ByVal WhichOne As System.Integer _
) As System.Object
```

```

Dim instance As IMateLoadReference
Dim WhichOne As System.Integer
Dim value As System.Object
 
value = instance.GetFaces(WhichOne)
```

```

System.object GetFaces( 
   System.int WhichOne
)
```

```

System.Object^ GetFaces( 
   System.int WhichOne
) 
```

#### Parameters

*WhichOne*
:   - 0 = Component1

    1 = Component2

#### Return Value

Array of supplemental [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

Remarks

The supplemental faces can belong to one of two components. Specify the component that owns the supplemental faces that you want to access.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.md)  
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.md)  
[IMateLoadReference::GetFacesCount Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~GetFacesCount.md)  
[IMateLoadReference::IGetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~IGetFaces.md)
