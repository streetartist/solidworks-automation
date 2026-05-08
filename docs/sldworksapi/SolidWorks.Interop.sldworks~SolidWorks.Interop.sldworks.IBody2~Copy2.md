# Copy2 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2~Copy2`

Gets a copy of this body.
Gets a copy of this body.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function Copy2( _
   ByVal PreserveFaceIDs As System.Boolean _
) As System.Object
```

```

Dim instance As IBody2
Dim PreserveFaceIDs As System.Boolean
Dim value As System.Object
 
value = instance.Copy2(PreserveFaceIDs)
```

```

System.object Copy2( 
   System.bool PreserveFaceIDs
)
```

```

System.Object^ Copy2( 
   System.bool PreserveFaceIDs
) 
```

#### Parameters

*PreserveFaceIDs*
:   True to copy face IDs, false to create new IDs

#### Return Value

Copied IBody2

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IBody2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2.md)  
[IBody2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IBody2_members.md)
