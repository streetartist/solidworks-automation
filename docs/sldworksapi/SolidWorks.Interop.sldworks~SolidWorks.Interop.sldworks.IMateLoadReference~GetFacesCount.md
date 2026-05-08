# GetFacesCount Method (IMateLoadReference)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~GetFacesCount`

Gets the number of supplemental faces of the mate associated with the specified component.
Gets the number of supplemental faces of the mate associated with the specified component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetFacesCount( _
   ByVal WhichOne As System.Integer _
) As System.Integer
```

```

Dim instance As IMateLoadReference
Dim WhichOne As System.Integer
Dim value As System.Integer
 
value = instance.GetFacesCount(WhichOne)
```

```

System.int GetFacesCount( 
   System.int WhichOne
)
```

```

System.int GetFacesCount( 
   System.int WhichOne
) 
```

#### Parameters

*WhichOne*
:   - 0 = Component1
    - 1 = Component2

#### Return Value

Number of supplemental faces of the mate associated with the specified component

Remarks

The supplemental faces can belong to one of two components. Specify the component that owns the supplemental faces that you want to access.

Call this method before calling [IMateLoadReference::IGetFaces](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~IGetFaces.md) to determine the size of the array.

Example

[Insert Mate Load Reference (C#)](Insert_Mate_Load_Reference_Example_CSharp.htm)  
[Insert Mate Load Reference (VB.NET)](Insert_Mate_Load_Reference_Example_VBNET.htm)  
[Insert Mate Load Reference (VBA)](Insert_Mate_Load_Reference_Example_VB.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMateLoadReference Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference.md)  
[IMateLoadReference Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference_members.md)  
[IMateLoadReference::GetFaces Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMateLoadReference~GetFaces.md)
