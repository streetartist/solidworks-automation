# AddPLMComponent Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddPLMComponent`

Adds the specified component from a 3DEXPERIENCE collaborative space to the specified location in this assembly in SOLIDWORKS Connected.
Adds the specified component from a 3DEXPERIENCE collaborative space to the specified location in this assembly in [SOLIDWORKS Connected](ms-its:sldworksapiprogguide.chm:://Overview/SOLIDWORKS_Connected.htm).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddPLMComponent( _
   ByVal PLMID As System.String, _
   ByVal ConfigName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim PLMID As System.String
Dim ConfigName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As System.Object
 
value = instance.AddPLMComponent(PLMID, ConfigName, X, Y, Z)
```

```

System.object AddPLMComponent( 
   System.string PLMID,
   System.string ConfigName,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

System.Object^ AddPLMComponent( 
   System.String^ PLMID,
   System.String^ ConfigName,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*PLMID*
:   Unique ID of a component

*ConfigName*
:   Name of the configuration (Physical Product) from which to load the component

*X*
:   X-coordinate of the component center

*Y*
:   Y-coordinate of the component center

*Z*
:   Z-coordinate of the component center

#### Return Value

[IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::ReplacePLMComponents Method ()](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplacePLMComponents.md)
