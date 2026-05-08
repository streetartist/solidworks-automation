# AddLightToScene Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddLightToScene`

Adds a light source to a scene.
Adds a light source to a scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddLightToScene( _
   ByVal LpszNewValue As System.String _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim LpszNewValue As System.String
Dim value As System.Integer
 
value = instance.AddLightToScene(LpszNewValue)
```

```

System.int AddLightToScene( 
   System.string LpszNewValue
)
```

```

System.int AddLightToScene( 
   System.String^ LpszNewValue
) 
```

#### Parameters

*LpszNewValue*
:   Name to use for the light

#### Return Value

ID of the light

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
