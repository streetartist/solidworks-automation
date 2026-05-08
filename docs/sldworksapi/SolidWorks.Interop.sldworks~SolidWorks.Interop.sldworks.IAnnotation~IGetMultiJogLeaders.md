# IGetMultiJogLeaders Method (IAnnotation)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~IGetMultiJogLeaders`

Gets the multi-jog leaders on this annotation.
Gets the multi-jog leaders on this annotation.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function IGetMultiJogLeaders( _
   ByVal Count As System.Integer _
) As MultiJogLeader
```

```

Dim instance As IAnnotation
Dim Count As System.Integer
Dim value As MultiJogLeader
 
value = instance.IGetMultiJogLeaders(Count)
```

```

MultiJogLeader IGetMultiJogLeaders( 
   System.int Count
)
```

```

MultiJogLeader^ IGetMultiJogLeaders( 
   System.int Count
) 
```

#### Parameters

*Count*
:   Number of multi-jog leaders on this annotation

#### Return Value

- in-process, unmanaged C++: Pointer to an array of the [multi-jog leaders](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IMultiJogLeader.md)

- VBA, VB.NET, C#, and C++/CLI: Not supported

See [In-process Methods](sldworksapiprogguide.chm::/OVERVIEW/In-process_Methods.htm) for details about this type of method.

Remarks

Before calling this method, call [IAnnotation::GetMultiJogLeaderCount](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaderCount.md) to get Count.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAnnotation Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation.md)  
[IAnnotation Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation_members.md)  
[IAnnotation::GetMultiJogLeaders Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAnnotation~GetMultiJogLeaders.md)
