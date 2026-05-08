# AddSmartComponent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddSmartComponent`

Adds the specified component at the specified coordinates as a Smart Component to this assembly.
Adds the specified component at the specified coordinates as a Smart Component to this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddSmartComponent( _
   ByVal CompName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As Component2
```

```

Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As Component2
 
value = instance.AddSmartComponent(CompName, X, Y, Z)
```

```

Component2 AddSmartComponent( 
   System.string CompName,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

Component2^ AddSmartComponent( 
   System.String^ CompName,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*CompName*
:   Path and filename of the part document to add as a Smart Component

*X*
:   X coordinate for the Smart Component

*Y*
:   Y coordinate for the Smart Component

*Z*
:   Z coordinate for the Smart Component

#### Return Value

[Smart Component](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::CreateSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~CreateSmartComponent.md)  
[IComponent2::GetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~GetSmartComponentData.md)  
[IComponent2::IsSmartComponent Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsSmartComponent.md)  
[IComponent2::SetSmartComponentData Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~SetSmartComponentData.md)  
[ISmartComponentFeatureData Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISmartComponentFeatureData.md)
