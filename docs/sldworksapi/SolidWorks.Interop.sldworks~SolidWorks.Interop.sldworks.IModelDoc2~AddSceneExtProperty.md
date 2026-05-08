# AddSceneExtProperty Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~AddSceneExtProperty`

Stores a float, string, or integer value for a scene.
Stores a float, string, or integer value for a scene.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSceneExtProperty( _
   ByVal PropertyExtension As System.Object _
) As System.Integer
```

```

Dim instance As IModelDoc2
Dim PropertyExtension As System.Object
Dim value As System.Integer
 
value = instance.AddSceneExtProperty(PropertyExtension)
```

```

System.int AddSceneExtProperty( 
   System.object PropertyExtension
)
```

```

System.int AddSceneExtProperty( 
   System.Object^ PropertyExtension
) 
```

#### Parameters

*PropertyExtension*
:   Value for the scene

#### Return Value

Unique identifier returned to access the property extension in the future

Remarks

This scene extension property is stored on the model document, but is unique to the model's scene. To add the extension property, you must first define the VARIANT type (float, string, or integer), give your variable a value, and then call this method to place the value on the light source for future reference.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)
