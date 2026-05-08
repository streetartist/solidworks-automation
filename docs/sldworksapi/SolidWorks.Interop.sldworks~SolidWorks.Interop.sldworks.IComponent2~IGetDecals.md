# IGetDecals Method (IComponent2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IGetDecals`

Gets the decals applied to this component.
Gets the decals applied to this component.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetDecals( _
   ByVal Count As System.Integer _
) As Decal
```

```

Dim instance As IComponent2
Dim Count As System.Integer
Dim value As Decal
 
value = instance.IGetDecals(Count)
```

```

Decal IGetDecals( 
   System.int Count
)
```

```

Decal^ IGetDecals( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of decals

#### Return Value

- in-process, unmanaged C++: Pointer to an array of [decals](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IDecal.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IComponent2::GetDecalsCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetDecalsCount.md) to get the value of Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IComponent2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)  
[IComponent2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2_members.md)  
[IComponent2::GetDecals Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetDecals.md)
