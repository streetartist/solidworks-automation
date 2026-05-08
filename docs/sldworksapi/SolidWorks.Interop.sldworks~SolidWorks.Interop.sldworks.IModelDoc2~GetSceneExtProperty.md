# GetSceneExtProperty Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetSceneExtProperty`

Gets a float, string, or integer value stored for the scene.
Gets a float, string, or integer value stored for the scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetSceneExtProperty( _
   ByVal PropertyId As System.Integer _
) As System.Object
```

```

Dim instance As IModelDoc2
Dim PropertyId As System.Integer
Dim value As System.Object
 
value = instance.GetSceneExtProperty(PropertyId)
```

```

System.object GetSceneExtProperty( 
   System.int PropertyId
)
```

```

System.Object^ GetSceneExtProperty( 
   System.int PropertyId
) 
```

#### Parameters

*PropertyId*
:   ID of the property extension

#### Return Value

Value stored for the scene extension property

Remarks

The type returned is based on the how the data was placed. See [IModelDoc2::AddSceneExtProperty](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddSceneExtProperty.md) for deatails.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::ResetSceneExtProperty Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~ResetSceneExtProperty.md)
