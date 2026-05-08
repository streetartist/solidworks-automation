# IGetFaces Method (IMateLoadReference)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~IGetFaces`

Gets the supplemental faces of the mate associated with the specified component.
Gets the supplemental faces of the mate associated with the specified component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetFaces( _
   ByVal WhichOne As System.Integer, _
   ByVal FaceCount As System.Integer _
) As Face2
```

```

Dim instance As IMateLoadReference
Dim WhichOne As System.Integer
Dim FaceCount As System.Integer
Dim value As Face2
 
value = instance.IGetFaces(WhichOne, FaceCount)
```

```

Face2 IGetFaces( 
   System.int WhichOne,
   System.int FaceCount
)
```

```

Face2^ IGetFaces( 
   System.int WhichOne,
   System.int FaceCount
) 
```

#### Parameters

*WhichOne*
:   - 0 = Component1
    - 1 = Component2

*FaceCount*
:   Number of supplemental faces

#### Return Value

- in-process, unmanaged C++: Pointer to an array of supplemental [faces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IFace2.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

The supplemental faces can belong to one of two components. Specify the component that owns the supplemental faces that you want to access.

Before calling this method, call [IMateLoadReference::GetFacesCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~GetFacesCount.md) to determine the size of the array for that method.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.md)  
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.md)  
[IMateLoadReference::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~GetFaces.md)
