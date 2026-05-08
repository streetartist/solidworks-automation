# MirrorComponents Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MirrorComponents`

Obsolete. Superseded by IAssemblyDoc::MirrorComponents2.
Obsolete. Superseded by [IAssemblyDoc::MirrorComponents2.](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~MirrorComponents2.md)

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function MirrorComponents( _
   ByVal Plane As System.Object, _
   ByVal ComponentsToInstance As System.Object, _
   ByVal ComponentsToMirror As System.Object, _
   ByVal MirroredComponentFilenames As System.Object, _
   ByVal RecreateMates As System.Boolean, _
   ByVal ComponentModifier As System.Integer, _
   ByVal ComponentNameModifier As System.String, _
   ByVal MirroredFileLocation As System.String, _
   ByVal CopyCustomProperties As System.Boolean _
) As System.Object
```

```

Dim instance As IAssemblyDoc
Dim Plane As System.Object
Dim ComponentsToInstance As System.Object
Dim ComponentsToMirror As System.Object
Dim MirroredComponentFilenames As System.Object
Dim RecreateMates As System.Boolean
Dim ComponentModifier As System.Integer
Dim ComponentNameModifier As System.String
Dim MirroredFileLocation As System.String
Dim CopyCustomProperties As System.Boolean
Dim value As System.Object
 
value = instance.MirrorComponents(Plane, ComponentsToInstance, ComponentsToMirror, MirroredComponentFilenames, RecreateMates, ComponentModifier, ComponentNameModifier, MirroredFileLocation, CopyCustomProperties)
```

```

System.object MirrorComponents( 
   System.object Plane,
   System.object ComponentsToInstance,
   System.object ComponentsToMirror,
   System.object MirroredComponentFilenames,
   System.bool RecreateMates,
   System.int ComponentModifier,
   System.string ComponentNameModifier,
   System.string MirroredFileLocation,
   System.bool CopyCustomProperties
)
```

```

System.Object^ MirrorComponents( 
   System.Object^ Plane,
   System.Object^ ComponentsToInstance,
   System.Object^ ComponentsToMirror,
   System.Object^ MirroredComponentFilenames,
   System.bool RecreateMates,
   System.int ComponentModifier,
   System.String^ ComponentNameModifier,
   System.String^ MirroredFileLocation,
   System.bool CopyCustomProperties
) 
```

#### Parameters

*Plane*
:   Plane or planar face about which to mirror the components

*ComponentsToInstance*
:   Array of instances of the component to mirror

*ComponentsToMirror*
:   Array of [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md) to mirror

*MirroredComponentFilenames*
:   Array of filenames for the newly created mirrored assemblies or parts

*RecreateMates*
:   True to preserve any mates between the selected components if more than one component is to be mirrored, false to not

*ComponentModifier*
:   Prefix or suffix for the newly mirrored components if MirroredComponentFilenames is not specified, as defined by [swMirrorComponentNameModifier\_e](ms-help://SolidWorks.Interop.swconst/SolidWorks/SOLIDWORKS.Interop.swconst~SOLIDWORKS.Interop.swconst.swMirrorComponentNameModifier_e.html)

*ComponentNameModifier*
:   String to add to the prefix or suffix of the name of the newly mirrored component if MirroredComponentFilenames is not specified

*MirroredFileLocation*
:   Name of the folder where to store the file of the newly created mirrored components

*CopyCustomProperties*
:   True to copy the custom properties from the selected components to the mirrored components, false to not

#### Return Value

Array of the newly created [components](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)
