# AddComponent4 Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent4`

Obsolete. Superseded by IAssemblyDoc::AddComponent5.
Obsolete. Superseded by [IAssemblyDoc::AddComponent5](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent5.md).

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function AddComponent4( _
   ByVal CompName As System.String, _
   ByVal ConfigName As System.String, _
   ByVal X As System.Double, _
   ByVal Y As System.Double, _
   ByVal Z As System.Double _
) As Component2
```

```

Dim instance As IAssemblyDoc
Dim CompName As System.String
Dim ConfigName As System.String
Dim X As System.Double
Dim Y As System.Double
Dim Z As System.Double
Dim value As Component2
 
value = instance.AddComponent4(CompName, ConfigName, X, Y, Z)
```

```

Component2 AddComponent4( 
   System.string CompName,
   System.string ConfigName,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

Component2^ AddComponent4( 
   System.String^ CompName,
   System.String^ ConfigName,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*CompName*
:   Path name of a loaded part or assembly to add as a component (see **Remarks**)

*ConfigName*
:   Name of the configuration from which to load the component (see Remarks)

*X*
:   X coordinate of the component center

*Y*
:   Y coordinate of the component center

*Z*
:   Z coordinate of the component center

#### Return Value

[IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

The specified file must be loaded in memory. A file is loaded into memory when you load the file in your SOLIDWORKS session ([ISldWorks::OpenDoc6](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.ISldWorks~OpenDoc6.md)) or open an assembly that already contains the file.

If configName is empty or specifies a configuration that does not exist, then the current configuration  is used.

If you want to add the component at a position relative to the root component, use [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md) to reposition the component immediately after calling this method. Or, you can use [IAssemblyDoc::AddComponents](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents.md) or [IAssemblyDoc::AddComponents2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents2.md) to specify the transform when inserting a component, insert as many components as you want at once, and rotate and scale the component through the transform matrix.

IMPORTANT: The x, y, and z parameters of this method are relative to the bounding box of the component. Only use this method if you want to approximately position the component. Use IComponent2::Transform2 if you want to more precisely position the component.

Example

[Add Component and Mate (C++)](Add_Component_and_Mate_Example_CPlusPlus_COM.htm)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IAssemblyDoc::InsertEnvelope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertEnvelope.md)  
[IAssemblyDoc::ReplaceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents.md)
