# ICreateVector Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~ICreateVector`

Creates a math vector.
Creates a math vector.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function ICreateVector( _
   ByRef ArrayDataIn As System.Double _
) As MathVector
```

```

Dim instance As IMathUtility
Dim ArrayDataIn As System.Double
Dim value As MathVector
 
value = instance.ICreateVector(ArrayDataIn)
```

```

MathVector ICreateVector( 
   ref System.double ArrayDataIn
)
```

```

MathVector^ ICreateVector( 
   System.double% ArrayDataIn
) 
```

#### Parameters

*ArrayDataIn*
:   - in-process, unmanaged C++: Pointer to an array of doubles representing the x,y,z components of the vector

    - VBA, VB.NET, C#, and C++/CLI: Not supported

    See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

#### Return Value

Newly created [math vector](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathVector.md) or NULL if the operation fails

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IMathUtility Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility.md)  
[IMathUtility Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility_members.md)  
[IMathUtility::CreateVector Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMathUtility~CreateVector.md)
