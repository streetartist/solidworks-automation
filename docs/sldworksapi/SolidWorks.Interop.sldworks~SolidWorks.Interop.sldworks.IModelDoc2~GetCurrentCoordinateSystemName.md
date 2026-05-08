# GetCurrentCoordinateSystemName Method (IModelDoc2)

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~GetCurrentCoordinateSystemName`

Gets the name of the current coordinate system or an empty string for the default coordinate system.
Gets the name of the current coordinate system or an empty string for the default coordinate system.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function GetCurrentCoordinateSystemName() As System.String
```

```

Dim instance As IModelDoc2
Dim value As System.String
 
value = instance.GetCurrentCoordinateSystemName()
```

```

System.string GetCurrentCoordinateSystemName()
```

```

System.String^ GetCurrentCoordinateSystemName(); 
```

#### Return Value

Name of the current coordinate system

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IModelDoc2 Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2.md)  
[IModelDoc2 Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2_members.md)  
[IModelDoc2::InsertCoordinateSystem Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDoc2~InsertCoordinateSystem.md)  
[IModelDocExtension::GetCoordinateSystemTransformByName Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IModelDocExtension~GetCoordinateSystemTransformByName.md)
