# InsertEnvelope Method

Help ID: `SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~InsertEnvelope`

Adds an envelope in the specified configuration name in this assembly.
Adds an envelope in the specified configuration name in this assembly.

Syntax

- [Visual Basic (Declaration)](#i-syntax-VB)
- [Visual Basic (Usage)](#i-syntax-VBUsage)
- [C#](#i-syntax-CS)
- [C++/CLI](#i-syntax-CPP2005)

```

Function InsertEnvelope( _
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
 
value = instance.InsertEnvelope(CompName, ConfigName, X, Y, Z)
```

```

Component2 InsertEnvelope( 
   System.string CompName,
   System.string ConfigName,
   System.double X,
   System.double Y,
   System.double Z
)
```

```

Component2^ InsertEnvelope( 
   System.String^ CompName,
   System.String^ ConfigName,
   System.double X,
   System.double Y,
   System.double Z
) 
```

#### Parameters

*CompName*
:   Path and file name of file containing a part to insert as an envelope

*ConfigName*
:   Name of the configuration from which to load the envelope component

*X*
:   X coordinate of the center of the envelope component's bounding box

*Y*
:   Y coordinate of the center of the envelope component's bounding box

*Z*
:   Z coordinate of the center of the envelope component's bounding box

#### Return Value

[IComponent2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2.md)

Remarks

CompName does not have to be open before running this method. If it is not open, then this method opens it in a hidden state.

If ConfigName is empty or specifies a configuration that does not exist, then the current configuration is used.

The X, Y, Z parameters of this method are the center of the component bounding box. You must use [IComponent2::Transform2](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~Transform2.md) on the return interface pointer if you want to more precisely position the component.

Requirements

**Target Platforms:** Windows 7, Windows Vista SP1 or later, Windows XP SP3, Windows Server 2008 (Server Core not supported), Windows Server 2008 R2 (Server Core supported with SP1 or later), Windows Server 2003 SP2

See Also

#### Reference

[IAssemblyDoc Interface](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc.md)  
[IAssemblyDoc Members](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc_members.md)  
[IComponent2::IsEnvelope Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IComponent2~IsEnvelope.md)  
[IAssemblyDoc::AddComponent5 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponent5.md)  
[IAssemblyDoc::AddComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~AddComponents.md)  
[IAssemblyDoc::IAddComponents2 Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~IAddComponents2.md)  
[IAssemblyDoc::ReplaceComponents Method](SolidWorks.Interop.sldworks~SolidWorks.Interop.sldworks.IAssemblyDoc~ReplaceComponents.md)
